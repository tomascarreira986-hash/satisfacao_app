const buttons = document.querySelectorAll(".btn");
const message = document.getElementById("feedback-message");
let isLocked = false;
const TIMEOUT_MS = 3000; // 3 segundos

buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        if (isLocked) return;

        const satisfaction = btn.getAttribute("data-satisfaction");
        isLocked = true;

        fetch("/api/feedback", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({satisfaction})
        })
        .then(res => res.json())
        .then(() => {
            message.classList.remove("hidden");
            setTimeout(() => {
                message.classList.add("hidden");
                isLocked = false;
            }, TIMEOUT_MS);
        })
        .catch(() => {
            isLocked = false;
        });
    });
});
