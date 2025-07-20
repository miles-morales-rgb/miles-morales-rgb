const infoBox = document.getElementById("infoBox");
const planetName = document.getElementById("planetName");
const planetInfo = document.getElementById("planetInfo");
const planets = document.querySelectorAll(".planet");
const zoomContainer = document.getElementById("solarSystem");
const hoverSound = document.getElementById("hoverSound");
let zoomLevel = 1;

planets.forEach((planet) => {
  planet.addEventListener("click", () => {
    planetName.textContent = planet.getAttribute("data-name");
    planetInfo.textContent = planet.getAttribute("data-info");
    infoBox.style.display = "block";
  });

  planet.addEventListener("mouseenter", () => {
    hoverSound.currentTime = 0;
    hoverSound.play();
  });
});

document.getElementById("infoClose").onclick = () => {
  infoBox.style.display = "none";
};

function zoomIn() {
  zoomLevel += 0.1;
  document.querySelector(".solar-system").style.transform = \`scale(\${zoomLevel})\`;
}

function zoomOut() {
  zoomLevel -= 0.1;
  document.querySelector(".solar-system").style.transform = \`scale(\${zoomLevel})\`;
}
