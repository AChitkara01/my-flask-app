document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Thank you for reaching out! I will get back to you soon.");
 });
 document.querySelectorAll('.card-header').forEach(header => {
    header.addEventListener('click', function () {
        const card = this.closest('.card'); // Find the nearest parent card
        if (card) {
            card.classList.toggle('expanded'); // Toggle the expanded class
        }
    });
 }); 
 document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function(event) {
        event.preventDefault();
        const sectionId = this.getAttribute('href').substring(1);
        document.getElementById(sectionId).scrollIntoView({
            behavior: 'smooth'
        });
    });
 });
 
