// Category Filter Functionality
document.addEventListener('DOMContentLoaded', function () {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const appCards = document.querySelectorAll('.app-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            const category = this.dataset.category;

            // Update active button
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Filter cards
            appCards.forEach(card => {
                if (category === 'all' || card.dataset.category === category) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeIn 0.3s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
