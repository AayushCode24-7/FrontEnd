const URL = "http://127.0.0.1:5001";

async function getProducts() {
    try {
        const response = await fetch(`${URL}/products`);
        const data = await response.json();
        renderUI(data.products);
    } catch (error) {
        console.error("Error connecting to backend:", error);
    }
}

async function addToWatchlist(movie) {
    try {
        const response = await fetch(`${URL}/watchlist`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(movie)
        });
        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error("Failed to add:", error);
    }
}

function renderUI(arr) {
    const root = document.getElementById("root");
    root.innerHTML = "";
    
    arr.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <img src="${item.thumbnail}" />
            <div class="card-info">
                <h3>${item.title}</h3>
                <p>Rating: ${item.rating}</p>
                <button id="btn-${item.id}">+ Add to Watchlist</button>
            </div>
        `;
        root.appendChild(card);
        document.getElementById(`btn-${item.id}`).addEventListener("click", () => addToWatchlist(item));
    });
}

// Initial Call
getProducts();