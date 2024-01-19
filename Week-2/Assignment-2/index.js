const btn = document.querySelector(".btn");
const welcomeBlock = document.querySelector(".welcome-message");


btn.addEventListener("click", () => {
    const lowerContent = document.querySelector(".all-containers-2");
    lowerContent.style.display = "flex";
    lowerContent.style.flexFlow = "wrap";
    lowerContent.style.justifyContent = "center";
    lowerContent.style.gap = "10px";
    lowerContent.style.marginLeft = "auto";
    lowerContent.style.marginRight = "auto";
    lowerContent.style.marginTop = "15px";
});

welcomeBlock.addEventListener("click", () => {
    welcomeBlock.innerHTML = "Have a good Time!";
})