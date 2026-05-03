const URL = "http://127.0.0.1:5003";

document.addEventListener("DOMContentLoaded", () => {
    getmovies();
});

async function getmovies() {
    try {
        const response = await fetch(`${URL}/movies`);
        const data = await response.json();
        renderUI(data.movies);
    } catch (error) {
        console.error("Error:", error);
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
        alert("Server error.");
    }
}

// NEW: Function to delete from DB and refresh UI
async function removeFromWatchlist(title) {
    try {
        const response = await fetch(`${URL}/watchlist/${encodeURIComponent(title)}`, {
            method: "DELETE"
        });
        const result = await response.json();
        alert(result.message);
        getWatchlist(); // Refresh the list immediately
    } catch (error) {
        console.error("Delete failed:", error);
    }
}

async function getWatchlist() {
    try {
        const response = await fetch(`${URL}/watchlist`);
        const data = await response.json();
        renderWatchlist(data.watchlist);
    } catch (error) {
        console.error("Error:", error);
    }
}

function showHome() {
    document.getElementById("root").style.display = "flex";
    document.getElementById("watchlist-root").style.display = "none";
    getmovies();
}

function showWatchlist() {
    document.getElementById("root").style.display = "none";
    document.getElementById("watchlist-root").style.display = "flex";
    getWatchlist();
}

function renderUI(arr) {
    const root = document.getElementById("root");
    root.innerHTML = "";
    arr.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <img src="${item.thumbnail}" alt="${item.title}" />
            <div class="card-info">
                <h3>${item.title}</h3>
                <p>Rating: ${item.rating}✨</p>
                <button onclick='addToWatchlist(${JSON.stringify(item)})'>+ Watchlist</button>
            </div>
        `;
        root.appendChild(card);
    });
}

function renderWatchlist(arr) {
    const watchlistRoot = document.getElementById("watchlist-root");
    watchlistRoot.innerHTML = ""; 

    if (!arr || arr.length === 0) {
        watchlistRoot.innerHTML = "<p style='padding:20px;'>Your watchlist is empty.</p>";
        return;
    }

    arr.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <img src="${item.thumbnail}" alt="${item.title}" />
            <div class="card-info">
                <h3>${item.title}</h3>
                <p>Rating: ${item.rating}✨</p>
                <button class="delete-btn" onclick="removeFromWatchlist('${item.title}')">Remove 🗑️</button>
            </div>
        `;
        watchlistRoot.appendChild(card);
    });
}