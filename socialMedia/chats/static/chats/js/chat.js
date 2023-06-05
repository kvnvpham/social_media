let icon = document.querySelector('i.chat-icon');

function changeIconColor() {
    icon.style.color = '#0f766e';
}

function returnIconColor() {
    icon.style.color = '#14b8a6';
}

let chatWindow = document.querySelector('div.chat-window');
chatWindow.scrollTo(0, chatWindow.scrollHeight)

function scrollToBottom() {
    chatWindow.scrollTo(0, chatWindow.scrollHeight)
}