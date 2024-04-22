let searchForm = document.getElementById('search-form');

searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log('Search form was submitted');

    let searchQuery = document.getElementById('search-input').value;

    // Fetch call to search members
    fetch(`http://127.0.0.1:8000/api/members/search/?title=${searchQuery}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // Include additional headers if needed
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('SEARCH RESULTS:', data);
        displaySearchResults(data);
        // Handle search results as needed
    })
    .catch(error => {
        console.error('Error searching members:', error);
    });
});


function displaySearchResults(results) {
    console.log('1');
    let searchResultsDiv = document.getElementById('search-results');
    searchResultsDiv.innerHTML = ''; // Clear previous search results

    if (results.length > 0) {
        results.forEach(result => {
            let resultDiv = document.createElement('div');
            resultDiv.textContent = `Title: ${result.title}, Body: ${result.body}`;
            searchResultsDiv.appendChild(resultDiv);
        });
    } else {
        let noResultsDiv = document.createElement('div');
        noResultsDiv.textContent = 'No results found';
        searchResultsDiv.appendChild(noResultsDiv);
    }
}