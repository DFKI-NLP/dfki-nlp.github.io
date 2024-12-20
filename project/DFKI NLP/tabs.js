document.addEventListener('DOMContentLoaded', () => {
  // Select all tab buttons and contents
  const tabs = document.querySelectorAll('.tab-link');
  const contents = document.querySelectorAll('.tab-content');

  // Add event listener to each tab button
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Remove active class from all tabs and contents
      tabs.forEach(t => t.classList.remove('active'));
      contents.forEach(content => content.classList.remove('active'));

      // Add active class to the clicked tab and corresponding content
      tab.classList.add('active');
      const target = tab.getAttribute('data-tab');
      document.getElementById(target).classList.add('active');
    });
  });
});

const carousel = document.querySelector('.slt-carousel');
const prevButton = document.querySelector('#prev');
const nextButton = document.querySelector('#next');

prevButton.addEventListener('click', () => {
  carousel.scrollBy({ left: -300, behavior: 'smooth' });
});

nextButton.addEventListener('click', () => {
  carousel.scrollBy({ left: 300, behavior: 'smooth' });
});


// Detect Time and Greet User
const greetingMessage = document.getElementById('greeting-message');
const namePrompt = document.getElementById('name-prompt');
const usernameInput = document.getElementById('username');
const greetBtn = document.getElementById('greet-btn');

// Get current time and generate greeting
const getGreeting = () => {
  const hours = new Date().getHours();
  if (hours < 12) return 'Good Morning';
  if (hours < 18) return 'Good Afternoon';
  return 'Good Evening';
};

// Show greeting with user's name
greetBtn.addEventListener('click', () => {
  const username = usernameInput.value.trim();
  if (username) {
    greetingMessage.textContent = `${getGreeting()}, ${username}!`;
    namePrompt.style.display = 'none';
  } else {
    alert('Please enter your name.');
  }
});

// Initialize greeting
greetingMessage.textContent = `${getGreeting()}!`;





// Tab Functionality for Projects Page
document.addEventListener('DOMContentLoaded', () => {
  const tabLinks = document.querySelectorAll('.tab-link');
  const tabContents = document.querySelectorAll('.tab-content');

  tabLinks.forEach(link => {
    link.addEventListener('click', () => {
      // Remove active class from all tabs and tab contents
      tabLinks.forEach(tab => tab.classList.remove('active'));
      tabContents.forEach(content => content.classList.remove('active'));

      // Add active class to clicked tab and corresponding tab content
      link.classList.add('active');
      document.querySelector(`#${link.getAttribute('data-tab')}`).classList.add('active');
    });
  });
});


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});


document.querySelectorAll('.tab-link').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('.tab-content').forEach(content => {
      content.classList.remove('fade-in');
    });
    setTimeout(() => {
      document.querySelector(`#${button.dataset.tab}`).classList.add('fade-in');
    }, 100);
  });
});




