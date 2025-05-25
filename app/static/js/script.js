document.addEventListener("DOMContentLoaded", () => {
    const textBtn = document.getElementById("textMethodBtn");
    const fileBtn = document.getElementById("fileMethodBtn");

    const fileContainer = document.getElementById("uploadContainer");
    const textContainer = document.getElementById("textContainer");
    const submitBtn = document.getElementById("submitBtn");

    let useTextInput = false;

    textBtn.addEventListener("click", () => {
        useTextInput = true;
        fileContainer.style.display = useTextInput ? "none" : "flex";
        textContainer.style.display = useTextInput ? "flex" : "none";
        textBtn.classList.add("active_method");
        fileBtn.classList.remove("active_method");
    });


    fileBtn.addEventListener("click", () => {
        useTextInput = false;
        fileContainer.style.display = useTextInput ? "none" : "flex";
        textContainer.style.display = useTextInput ? "flex" : "none";
        fileBtn.classList.add("active_method");
        textBtn.classList.remove("active_method");
    });


    submitBtn.addEventListener("click", async () => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = '<div class="loader"></div>';

        let formData = new FormData();

        if (useTextInput) {
            const code = document.getElementById("codeInput").value;
            formData.append("code", code);
        } else {
            const file = document.getElementById("codefile").files[0];
            if (!file) return alert("Please upload a file.");
            formData.append("codefile", file);
        }

        const response = await fetch("/solid", {
            method: "POST",
            body: formData,
        });

        const data = await response.text();
        resultDiv.innerHTML = data;
        window.scrollTo({
            top: resultDiv.offsetTop,
            behavior: "smooth"
        });
    });
});
