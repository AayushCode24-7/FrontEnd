const URL = "http://127.0.0.1:5003";

// 1. Initial Load
document.addEventListener("DOMContentLoaded", () => {
    getmovies();
});

// 2. Fetch Movies for Home Page
async function getmovies() {
    try {
        const response = await fetch(`${URL}/movies`);
        const data = await response.json();
        renderUI(data.movies);
    } catch (error) {
        console.error("Error connecting to backend:", error);
    }
}

// 3. Add a Movie to the Watchlist
async function addToWatchlist(movie) {
    try {
        const response = await fetch(`${URL}/watchlist`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(movie)
        });
        const result = await response.json();
        
        // Alert user if success or duplicate
        alert(result.message);
        
    } catch (error) {
        console.error("Failed to add:", error);
        alert("Server error. Could not add movie.");
    }
}

// 4. Fetch Watchlist from Backend
async function getWatchlist() {
    try {
        const response = await fetch(`${URL}/watchlist`);
        const data = await response.json();
        renderWatchlist(data.watchlist);
    } catch (error) {
        console.error("Error fetching watchlist:", error);
    }
}

// 5. Navigation Logic (Switching Views)
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

// 6. UI Rendering for Home Page
function renderUI(arr) {
    const root = document.getElementById("root");
    root.innerHTML = "";
    
    if (!arr || arr.length === 0) {
        root.innerHTML = "<p>No movies found.</p>";
        return;
    }

    arr.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <img src="${item.thumbnail}" alt="${item.title}" />
            <div class="card-info">
                <h3>${item.title}</h3>
                <p> Rating: ${item.rating}✨</p>
                <button id="btn-${item.id}">+ Add to Watchlist</button>
            </div>
        `;
        root.appendChild(card);
        // Add event listener to the button
        document.getElementById(`btn-${item.id}`).addEventListener("click", () => addToWatchlist(item));
    });
}

// 7. UI Rendering for Watchlist Page (The Fixed Function)
function renderWatchlist(arr) {
    const watchlistRoot = document.getElementById("watchlist-root");
    watchlistRoot.innerHTML = ""; // Clear existing content
    
    // Add a heading for the section
    // const heading = document.createElement("h2");
    // heading.innerText = "My Watchlist";
    // heading.style.width = "100%";
    // heading.style.padding = "20px";
    // watchlistRoot.appendChild(heading);

    if (!arr || arr.length === 0) {
        const msg = document.createElement("p");
        msg.innerText = "Your watchlist is empty.";
        msg.style.padding = "20px";
        watchlistRoot.appendChild(msg);
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
            </div>
        `;
        watchlistRoot.appendChild(card);
    });

}