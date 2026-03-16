const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");
const input = document.getElementById("user-input");

function addMessage(message, type) {
  const msg = document.createElement("div");
  msg.classList.add("chat-message");

  if (type === "user") {
    msg.classList.add("user-message");
    msg.innerText = message;
  }

  if (type === "bot") {
    msg.classList.add("bot-message");
    msg.innerHTML = marked.parse(message, { breaks: true });
  }

  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

if (chatBox.children.length === 0) {
  addMessage(
    "👋 Hello! I'm the **ArogyaFasal Assistant**. Ask me about crop diseases, fertilizers, or farming tips.",
    "bot",
  );
}

function showTyping() {
  const typing = document.createElement("div");

  typing.id = "typing";
  typing.innerHTML = `
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

  chatBox.appendChild(typing);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById("typing");

  if (typing) typing.remove();
}

sendBtn.onclick = async () => {
  const message = input.value.trim();

  if (!message) return;

  addMessage(message, "user");
  input.value = "";
  showTyping();

  const response = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  removeTyping();
  addMessage(data.reply, "bot");
};

const chatToggle = document.getElementById("chat-toggle");
const chatWindow = document.getElementById("chat-window");

if (!chatToggle || !chatWindow) {
  console.warn("Chat widget elements not found");
} else {
  chatToggle.addEventListener("click", () => {
    if (chatWindow.style.display === "flex") {
      chatWindow.style.display = "none";
    } else {
      chatWindow.style.display = "flex";
    }
  });
}

input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendBtn.click();
  }
});
