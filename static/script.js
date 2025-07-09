document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const chatMessages = document.getElementById('chat-messages');
    if (chatContainer && chatMessages) {
        chatContainer.insertBefore(chatMessages, chatContainer.firstChild);
    }
});

function createMessageElement(message, sender = 'user', isLoading = false) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('chat-message', sender);
    if (isLoading) {
        msgDiv.classList.add('loading');
    }
    msgDiv.innerHTML = message;
    return msgDiv;
}

function scrollChatToBottom() {
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.scrollTop = chatMessages.scrollHeight;
    // Ensure input stays visible
    const chatInput = document.querySelector('.chat-input');
    if (chatInput) {
        chatInput.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
}

document.getElementById('send-message').addEventListener('click', async () => {
    const messageInput = document.getElementById('chat-message');
    const message = messageInput.value;
    if (message.trim() === '') return;

    const chatMessages = document.getElementById('chat-messages');
    // Add user message
    const userMessage = createMessageElement(message, 'user');
    chatMessages.appendChild(userMessage);
    messageInput.value = '';
    // Add loading message
    const botMessage = createMessageElement('Loading...', 'bot', true);
    chatMessages.appendChild(botMessage);
    scrollChatToBottom();

    try {
        const response = await fetch('/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: message, top_n: 5 })
        });
        if (!response.ok) throw new Error('Failed to fetch response');
        const data = await response.json();
        // Format response beautifully (basic markdown support)
        botMessage.classList.remove('loading');
        botMessage.innerHTML = `<div class='bot-response'>${formatBotResponse(data.response)}</div>`;
        scrollChatToBottom();
    } catch (error) {
        botMessage.classList.remove('loading');
        botMessage.innerHTML = `<span style='color:red'>Error: ${error.message}</span>`;
        scrollChatToBottom();
    }
    chatMessages.scrollTop = chatMessages.scrollHeight;
    if (chatMessages.children.length > 0) {
        chatMessages.style.display = 'block';
    }
    scrollChatToBottom();
});

document.getElementById('chat-message').addEventListener('keypress', async (event) => {
    if (event.key === 'Enter') {
        document.getElementById('send-message').click();
    }
});

function formatBotResponse(text) {
    // Basic formatting: newlines to <br>, code blocks, bold, etc.
    let formatted = text
        .replace(/\n/g, '<br>')
        .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
        .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>')
        .replace(/\*(.*?)\*/g, '<i>$1</i>');
    return formatted;
}
