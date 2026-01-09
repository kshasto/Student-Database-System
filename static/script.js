// Live Search
function searchStudent() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let rows = document.querySelectorAll("table tbody tr");

    rows.forEach(row => {
        let text = row.innerText.toLowerCase();
        row.style.display = text.includes(input) ? "" : "none";
    });
}

// Delete Confirmation
function confirmDelete() {
    return confirm("Are you sure you want to delete this record?");
}

// Auto focus input
window.onload = function () {
    let firstInput = document.querySelector("form input");
    if (firstInput) {
        firstInput.focus();
    }
};
