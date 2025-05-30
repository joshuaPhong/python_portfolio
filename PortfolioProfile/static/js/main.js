/**
 * Main JavaScript file for Creative Portfolio
 * Handles interactions, animations, and enhancements
 */

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeScrollEffects();
    initializeImageLoading();
    initializeContactForm();
    initializeNavigation();
    initializeAnimations();
    
    console.log('Portfolio website initialized successfully');
});

/**
 * Scroll effects and animations
 */
function initializeScrollEffects() {
    // Add scroll-based navbar styling
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    
    function updateNavbar() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        } else {
            navbar.classList.remove('scrolled');
            navbar.style.background = '';
            navbar.style.backdropFilter = '';
        }
    }
    
    window.addEventListener('scroll', throttle(updateNavbar, 16));
    updateNavbar(); // Initial check
    
    // Smooth reveal animations for elements
    if ('IntersectionObserver' in window) {
        const revealElements = document.querySelectorAll('.card, .timeline-item, .skill-category');
        
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        entry.target.classList.add('fade-in');
                    }, index * 100); // Stagger animations
                    
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        revealElements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            revealObserver.observe(element);
        });
    }
}

/**
 * Enhanced image loading with lazy loading fallback
 */
function initializeImageLoading() {
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    // Add loading placeholder
    images.forEach(img => {
        const wrapper = img.parentElement;
        
        // Create loading placeholder
        const placeholder = document.createElement('div');
        placeholder.className = 'image-placeholder';
        placeholder.style.cssText = `
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            animation: loading 1.5s infinite;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666;
            font-size: 14px;
        `;
        
        // Add loading animation CSS if not exists
        if (!document.querySelector('#loading-animation')) {
            const style = document.createElement('style');
            style.id = 'loading-animation';
            style.textContent = `
                @keyframes loading {
                    0% { background-position: 200% 0; }
                    100% { background-position: -200% 0; }
                }
            `;
            document.head.appendChild(style);
        }
        
        placeholder.innerHTML = '<i data-feather="image"></i>';
        
        if (wrapper.style.position !== 'absolute' && wrapper.style.position !== 'relative') {
            wrapper.style.position = 'relative';
        }
        
        wrapper.appendChild(placeholder);
        
        // Handle image load
        const handleImageLoad = () => {
            img.style.opacity = '1';
            placeholder.remove();
            img.classList.add('fade-in');
            
            // Re-initialize feather icons
            if (window.feather) {
                feather.replace();
            }
        };
        
        const handleImageError = () => {
            placeholder.innerHTML = '<i data-feather="image-off"></i><div>Failed to load</div>';
            placeholder.style.background = '#f8f9fa';
            
            // Re-initialize feather icons
            if (window.feather) {
                feather.replace();
            }
        };
        
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.3s ease';
        
        if (img.complete) {
            handleImageLoad();
        } else {
            img.addEventListener('load', handleImageLoad);
            img.addEventListener('error', handleImageError);
        }
    });
}

/**
 * Contact form enhancements
 */
function initializeContactForm() {
    const contactForm = document.querySelector('.contact-form');
    if (!contactForm) return;
    
    const inputs = contactForm.querySelectorAll('input, textarea, select');
    
    // Enhanced validation
    inputs.forEach(input => {
        // Real-time validation
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            if (this.classList.contains('is-invalid')) {
                validateField(this);
            }
        });
    });
    
    // Form submission handling
    contactForm.addEventListener('submit', function(e) {
        let isValid = true;
        
        inputs.forEach(input => {
            if (!validateField(input)) {
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            showNotification('Please fix the errors in the form', 'error');
            return;
        }
        
        // Show loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        submitBtn.innerHTML = '<i data-feather="loader" class="me-2"></i>Sending...';
        submitBtn.disabled = true;
        
        // Re-initialize feather icons
        if (window.feather) {
            feather.replace();
        }
        
        // Handle form submission result (this would normally be handled by Flask)
        setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            
            if (window.feather) {
                feather.replace();
            }
        }, 2000);
    });
    
    function validateField(field) {
        const value = field.value.trim();
        let isValid = true;
        let message = '';
        
        // Remove existing feedback
        field.classList.remove('is-valid', 'is-invalid');
        const existingFeedback = field.parentElement.querySelector('.invalid-feedback');
        if (existingFeedback) {
            existingFeedback.remove();
        }
        
        // Required field validation
        if (field.hasAttribute('required') && !value) {
            isValid = false;
            message = 'This field is required';
        }
        
        // Email validation
        if (field.type === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                message = 'Please enter a valid email address';
            }
        }
        
        // Message length validation
        if (field.id === 'message' && value) {
            if (value.length < 10) {
                isValid = false;
                message = 'Message should be at least 10 characters long';
            }
        }
        
        // Apply validation styling
        if (isValid) {
            field.classList.add('is-valid');
        } else {
            field.classList.add('is-invalid');
            
            const feedback = document.createElement('div');
            feedback.className = 'invalid-feedback';
            feedback.textContent = message;
            field.parentElement.appendChild(feedback);
        }
        
        return isValid;
    }
}

/**
 * Navigation enhancements
 */
function initializeNavigation() {
    // Mobile menu handling
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.navbar') && navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
        
        // Close mobile menu when clicking on nav links
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }
    
    // Active navigation highlighting based on scroll position
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    
    if (sections.length && navLinks.length) {
        function updateActiveNav() {
            const scrollPos = window.scrollY + 100;
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                const sectionId = section.getAttribute('id');
                
                if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${sectionId}`) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }
        
        window.addEventListener('scroll', throttle(updateActiveNav, 16));
    }
}

/**
 * General animations and interactions
 */
function initializeAnimations() {
    // Parallax effect for hero sections
    const heroSections = document.querySelectorAll('.hero-section, .bg-gradient');
    
    heroSections.forEach(section => {
        window.addEventListener('scroll', throttle(() => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            section.style.transform = `translateY(${rate}px)`;
        }, 16));
    });
    
    // Enhanced hover effects for cards
    const cards = document.querySelectorAll('.card, .hover-lift');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Button click animations
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            
            ripple.style.cssText = `
                position: absolute;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.3);
                transform: scale(0);
                animation: ripple 0.6s linear;
                width: ${size}px;
                height: ${size}px;
                left: ${e.clientX - rect.left - size / 2}px;
                top: ${e.clientY - rect.top - size / 2}px;
            `;
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Add ripple animation CSS if not exists
    if (!document.querySelector('#ripple-animation')) {
        const style = document.createElement('style');
        style.id = 'ripple-animation';
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Utility function to show notifications
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type === 'error' ? 'danger' : 'success'} alert-dismissible fade show`;
    notification.innerHTML = `
        <i data-feather="${type === 'error' ? 'alert-circle' : 'check-circle'}" class="me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    notification.style.cssText = `
        position: fixed;
        top: 90px;
        right: 20px;
        z-index: 1050;
        max-width: 400px;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Re-initialize feather icons
    if (window.feather) {
        feather.replace();
    }
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
    
    // Add slide-in animation if not exists
    if (!document.querySelector('#slide-animation')) {
        const style = document.createElement('style');
        style.id = 'slide-animation';
        style.textContent = `
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Throttle function for performance optimization
 */
function throttle(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Debounce function for performance optimization
 */
function debounce(func, wait, immediate) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            timeout = null;
            if (!immediate) func(...args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func(...args);
    };
}

/**
 * Handle keyboard navigation
 */
document.addEventListener('keydown', function(e) {
    // ESC key to close modals/dropdowns
    if (e.key === 'Escape') {
        const dropdowns = document.querySelectorAll('.dropdown-menu.show');
        dropdowns.forEach(dropdown => {
            dropdown.classList.remove('show');
        });
        
        const navbarCollapse = document.querySelector('.navbar-collapse.show');
        if (navbarCollapse) {
            document.querySelector('.navbar-toggler').click();
        }
    }
    
    // Accessibility: Enter key on buttons
    if (e.key === 'Enter' && e.target.tagName === 'BUTTON') {
        e.target.click();
    }
});

/**
 * Handle focus management for accessibility
 */
document.addEventListener('focusin', function(e) {
    if (e.target.matches('input, textarea, select, button, a')) {
        e.target.classList.add('keyboard-focused');
    }
});

document.addEventListener('focusout', function(e) {
    e.target.classList.remove('keyboard-focused');
});

/**
 * Performance monitoring
 */
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(() => {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.fetchStart, 'ms');
        }, 0);
    });
}

/**
 * Error handling
 */
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    
    // Show user-friendly error message for critical errors
    if (e.error && e.error.message && !e.error.message.includes('Script error')) {
        showNotification('Something went wrong. Please refresh the page.', 'error');
    }
});

/**
 * Service worker registration for PWA features (future enhancement)
 */
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Uncomment and implement when service worker is ready
        // navigator.serviceWorker.register('/sw.js')
        //     .then(registration => console.log('SW registered'))
        //     .catch(error => console.log('SW registration failed'));
    });
}
