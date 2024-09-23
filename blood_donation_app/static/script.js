// script.js

function updateRegion() {
    var region = document.getElementById('region').value;
    var provinceSelect = document.getElementById('province');
    var municipalitySelect = document.getElementById('municipality');

    // Assuming you have a dictionary of regions, provinces, and municipalities
    var regions = {
        'Region III': {
            'Pampanga': ['Angeles City', 'Mabalacat City', 'San Fernando City'],
            'Bulacan': ['Malolos City', 'Meycauayan City', 'San Jose del Monte City']
        },
        'Region IV-A': {
            'Cavite': ['Bacoor City', 'Dasmariñas City', 'Imus City'],
            'Laguna': ['Biñan City', 'Calamba City', 'San Pablo City'],
        },
