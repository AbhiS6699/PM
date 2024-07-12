document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.mySwiper', {
        slidesPerView: 3,
        spaceBetween: 30,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        autoplay: {
            delay: 1500,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20,
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 3,
                spaceBetween: 30,
            },
        },
    });

    swiperContainer = document.querySelector('.mySwiper');

    // Pause autoplay on hover
    swiperContainer.addEventListener('mouseenter', function () {
        mySwiper.autoplay.stop();
    });

    // Resume autoplay when hover stops
    swiperContainer.addEventListener('mouseleave', function () {
        mySwiper.autoplay.start();
    });
});


var mySwiper1 = new Swiper('.mySwiper1', {
    slidesPerView: 4,
    spaceBetween: 30, // Adjust space between cards
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});


function toggleModal(show) {
    document.getElementById('modal-backdrop').style.display = show ? 'block' : 'none';
    document.getElementById('modal').style.display = show ? 'block' : 'none';
}

document.getElementById('submit-requirement-button').addEventListener('click', function () {
    toggleModal(true);
});

document.getElementById('close-modal').addEventListener('click', function () {
    toggleModal(false);
});



document.addEventListener('DOMContentLoaded', function () {
    // ... previous code remains unchanged ...
    const minBudgetSelect = document.getElementById('minBudget');
    const maxBudgetSelect = document.getElementById('maxBudget');
    const minBudgetInput = document.getElementById('minBudgetInput');
    const maxBudgetInput = document.getElementById('maxBudgetInput');

    const budgetOptions = [
        "2 lakh", "5 lakh", "10 lakh", "15 lakh", "20 lakh", "25 lakh", "30 lakh",
        "35 lakh", "40 lakh", "45 lakh", "50 lakh", "55 lakh", "60 lakh", "65 lakh",
        "70 lakh", "75 lakh", "80 lakh", "85 lakh", "90 lakh", "95 lakh", "1 Cr",
        "5 Cr", "10 Cr", "15 Cr", "20 Cr"
    ];

    // Populate the dropdowns with budget options
    budgetOptions.forEach(option => {
        minBudgetSelect.add(new Option(option, option));
        maxBudgetSelect.add(new Option(option, option));
    });

    // Sync the dropdowns with the manual inputs
    minBudgetSelect.addEventListener('change', function () {
        minBudgetInput.value = this.value;
    });

    maxBudgetSelect.addEventListener('change', function () {
        maxBudgetInput.value = this.value;
    });

    // Update dropdowns when manual input values are changed
    minBudgetInput.addEventListener('input', function () {
        if (budgetOptions.includes(this.value)) {
            minBudgetSelect.value = this.value;
        }
    });

    // Adjust the direction of the dropdowns if they open upwards
    function adjustDropdown(dropdown) {
        // Get the bounding rectangle of the dropdown
        var rect = dropdown.getBoundingClientRect();
        // Check if the dropdown is close to the bottom of the screen
        if (window.innerHeight - rect.bottom < rect.height) {
            // If there is not enough space for the dropdown to open downwards,
            // add enough space at the bottom of the content
            document.body.style.minHeight = `${window.innerHeight + rect.height}px`;
        }
    }

    minBudgetSelect.addEventListener('focus', function () {
        adjustDropdown(this);
    });

    maxBudgetSelect.addEventListener('focus', function () {
        adjustDropdown(this);
    });
});



// Toggle button active state
document.querySelectorAll('.toggle-button').forEach(button => {
    button.addEventListener('click', function () {
        button.classList.toggle('active');
    });
});

// Submit form data
document.getElementById('requirements-form').addEventListener('submit', function (event) {
    event.preventDefault();
    // Collect and send form data to server
});

// JavaScript to handle dropdown visibility on hover
document.querySelectorAll('.dropdown-toggle').forEach(item => {
    item.addEventListener('mouseover', function () {
        const dropdown = this.nextElementSibling;
        if (dropdown) {
            dropdown.style.display = 'block';
        }
    });
    item.addEventListener('mouseout', function () {
        const dropdown = this.nextElementSibling;
        if (dropdown) {
            dropdown.style.display = 'none';
        }
    });
});

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

document.getElementById('searchInput').addEventListener('input', function () {
    const inputVal = this.value.toLowerCase();
    const suggestionsContainer = document.getElementById('suggestionsContainer');

    // Simulate fetching data (this should be replaced with actual API calls in production)
    const data = [
        { name: "Sunshine Apartments", url: "/property/sunshine-apartments" },
        { name: "Greenwood Society", url: "/property/greenwood-society" },
        { name: "Builder Solutions Condo", url: "/property/builder-solutions-condo" }
    ];

    // Filter data based on input
    const matches = data.filter(item => item.name.toLowerCase().includes(inputVal));

    // Show suggestions
    suggestionsContainer.innerHTML = '';
    if (matches.length > 0 && inputVal !== '') {
        suggestionsContainer.classList.remove('hidden');
        matches.forEach(item => {
            const suggestionElement = document.createElement('div');
            suggestionElement.classList.add('p-2', 'hover:bg-gray-100', 'cursor-pointer');
            suggestionElement.textContent = item.name;
            suggestionElement.onclick = () => window.location.href = item.url;
            suggestionsContainer.appendChild(suggestionElement);
        });
    } else {
        suggestionsContainer.classList.add('hidden');
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.carousel-image');
    let currentImageIndex = 0;

    function changeImage() {
        images[currentImageIndex].style.display = 'none';
        currentImageIndex = (currentImageIndex + 1) % images.length;
        images[currentImageIndex].style.display = 'block';
    }

    // Set initial image display
    images[currentImageIndex].style.display = 'block';

    // Change image every 2000 milliseconds (2 seconds)
    setInterval(changeImage, 2000);
});







