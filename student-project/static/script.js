function toggleTheme() {
    document.body.classList.toggle("light-mode");
}

function searchTable() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {
        row.style.display = row.innerText.toLowerCase().includes(input)
            ? "" : "none";
    });
}
