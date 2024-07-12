document.addEventListener('DOMContentLoaded', (event) => {
    const wrapper = document.querySelector('.wrapper');
    const registerLink = document.querySelector('.register-link');
    const loginLink = document.querySelector('.login-link');

    if (registerLink) {
        registerLink.addEventListener('click', () => {
            console.log('clickkk');
            if (wrapper) {
                wrapper.classList.add('active');
            }
        });
    }
})