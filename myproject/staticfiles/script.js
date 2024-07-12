document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.mySwiper', {
        slidesPerView: 3,
        spaceBetween: 30,
        slidesPerGroup: 1,
        loop: true,
        loopFillGroupWithBlank: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
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
});

document.addEventListener('DOMContentLoaded', function() {
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
    minBudgetSelect.addEventListener('change', function() {
        minBudgetInput.value = this.value;
    });

    maxBudgetSelect.addEventListener('change', function() {
        maxBudgetInput.value = this.value;
    });

    // Update dropdowns when manual input values are changed
    minBudgetInput.addEventListener('input', function() {
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

    minBudgetSelect.addEventListener('focus', function() {
        adjustDropdown(this);
    });

    maxBudgetSelect.addEventListener('focus', function() {
        adjustDropdown(this);
    });
});


