const URL = "http://127.0.0.1:5001/products";

// Fetching data from the Backend
async function getProducts() {
    try {
        const response = await fetch(URL);
        const data = await response.json();
        renderUI(data.products);
    } catch (error) {
        console.log("Error: Backend is not running on port 5001");
    }
}

// Rendering the UI using the data
function renderUI(arr) {
    const root = document.getElementById("root");
    root.innerHTML = ""; // Clear old data
    
    arr.forEach((item) => {
        const card = document.createElement("div");
        card.style.border = "1px solid black"; // Simple styling from notes
        card.innerHTML = `
            <img src="${item.thumbnail}" width="200px" />
            <h3>${item.title}</h3>
            <p>Rating: ${item.rating}</p>
        `;
        root.appendChild(card);
    });
}

getProducts();