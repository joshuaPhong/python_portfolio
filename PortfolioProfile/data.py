"""
Project data management for the portfolio website.
In a production application, this would likely come from a database.
"""

# Project data using the provided stock photos
PROJECTS = [
    {
        'id': 1,
        'title': 'Creative Design Studio',
        'category': 'Web Design',
        'description': 'A modern creative studio website featuring bold typography and immersive visual storytelling.',
        'image': 'https://pixabay.com/get/gf09f6d798aacf7f86b7fc849dfc92e9fe63240cf026997ddaf7a5b01a18dde31a3abde75128adba71d16909158375e81d02b92be1751fecdc3be128f1ced2206_1280.jpg',
        'details': {
            'client': 'Creative Studio Inc.',
            'year': '2024',
            'technologies': ['HTML5', 'CSS3', 'JavaScript', 'GSAP'],
            'challenge': 'Create an engaging digital presence that showcases the studio\'s creative capabilities while maintaining fast loading times and accessibility.',
            'solution': 'Implemented a progressive loading system with optimized animations and semantic HTML structure for better SEO and accessibility.',
            'result': 'Increased client inquiries by 150% and improved user engagement metrics significantly.'
        }
    },
    {
        'id': 2,
        'title': 'Digital Marketing Dashboard',
        'category': 'UI/UX Design',
        'description': 'An intuitive dashboard interface for digital marketing analytics with real-time data visualization.',
        'image': 'https://pixabay.com/get/g86af6766baa6638c7d4ec63870d81174de7c305dd85c236cc1cfba9991ea8a59c327d22d93d35a469091b7952bfe970be74e3ee41dae48d0e3962cc0288e94a4_1280.jpg',
        'details': {
            'client': 'MarketingPro Analytics',
            'year': '2024',
            'technologies': ['React', 'D3.js', 'Node.js', 'MongoDB'],
            'challenge': 'Design a complex data interface that remains user-friendly while displaying comprehensive marketing metrics.',
            'solution': 'Created a modular dashboard system with customizable widgets and intuitive data filtering options.',
            'result': 'Reduced data analysis time by 60% and improved decision-making speed for marketing teams.'
        }
    },
    {
        'id': 3,
        'title': 'Startup Launch Platform',
        'category': 'Web Development',
        'description': 'A comprehensive platform for startup launches featuring investor connections and project showcasing.',
        'image': 'https://pixabay.com/get/g73a44dd11a9dc93de3302c744fb9f799a9597d547a634e0624158192613b934af10bd869483662baa95990245f49468e62fa72a1e04f7a82efa9cb77d3bbb16f_1280.jpg',
        'details': {
            'client': 'LaunchPad Ventures',
            'year': '2023',
            'technologies': ['Flask', 'PostgreSQL', 'Bootstrap', 'Stripe API'],
            'challenge': 'Build a scalable platform that connects startups with investors while managing sensitive financial data.',
            'solution': 'Implemented robust authentication, encrypted data storage, and a matching algorithm for startup-investor connections.',
            'result': 'Successfully facilitated over $2M in startup funding and onboarded 500+ users in the first quarter.'
        }
    },
    {
        'id': 4,
        'title': 'Photography Portfolio',
        'category': 'Creative Development',
        'description': 'An elegant photography portfolio with immersive galleries and booking functionality.',
        'image': 'https://pixabay.com/get/g0ba4d6e0770f3d85e37ddd0786f5397673efd45a35e23c78b15455e7d37d3bf09c953f905f6ce2fa6d22d051340656cbdcb25975862dcc4cf0cf754f290b240d_1280.jpg',
        'details': {
            'client': 'Sarah Chen Photography',
            'year': '2023',
            'technologies': ['Vue.js', 'Laravel', 'AWS S3', 'Lightbox'],
            'challenge': 'Create a visually stunning portfolio that loads quickly despite high-resolution images.',
            'solution': 'Implemented progressive image loading, lazy loading, and CDN integration for optimal performance.',
            'result': 'Increased booking inquiries by 200% and reduced page load times by 70%.'
        }
    },
    {
        'id': 5,
        'title': 'E-commerce Mobile App',
        'category': 'Mobile Development',
        'description': 'A feature-rich mobile shopping app with seamless payment integration and personalized recommendations.',
        'image': 'https://pixabay.com/get/g5557a62f90a9d88cb58a0946dcd784263a16bf1763d9a91174f46f7167536ba2ce803a88d88a493186d162451092d96b05c85508b0e445eaed160720a11976f7_1280.jpg',
        'details': {
            'client': 'ShopEasy Inc.',
            'year': '2024',
            'technologies': ['React Native', 'Node.js', 'Redis', 'PayPal API'],
            'challenge': 'Develop a cross-platform mobile app that provides native performance and user experience.',
            'solution': 'Built with React Native using native modules for performance-critical features and implemented offline caching.',
            'result': 'Achieved 4.8-star app store rating and 40% increase in mobile sales conversion.'
        }
    },
    {
        'id': 6,
        'title': 'Financial Planning Tool',
        'category': 'Web Application',
        'description': 'An interactive financial planning tool with budget tracking and investment portfolio management.',
        'image': 'https://pixabay.com/get/g4f1fdc725188e5664b60e4bc1d497d231a9def5b0c380117bc3393c71252cb37350a732eacbe87b09971b182453fc9fb45acfe39b82486c59b943a566b448fc2_1280.jpg',
        'details': {
            'client': 'WealthTracker Solutions',
            'year': '2023',
            'technologies': ['Django', 'Chart.js', 'Celery', 'Redis'],
            'challenge': 'Create a secure financial application that handles sensitive data while providing intuitive visualizations.',
            'solution': 'Implemented bank-level security protocols, real-time data synchronization, and interactive financial charts.',
            'result': 'Helped users save an average of $3,000 annually and manage portfolios worth over $10M collectively.'
        }
    },
    {
        'id': 7,
        'title': 'Responsive Web Design',
        'category': 'Frontend Development',
        'description': 'A cutting-edge responsive website showcasing modern CSS techniques and performance optimization.',
        'image': 'https://pixabay.com/get/g3a0ae916dbfdf2156bec90a187b5763f108259622df97ae664966e9183580514fd1a2456e18dcf6b7997552d3d95c4d10e11cdf015c8b0e4e829323be1216654_1280.jpg',
        'details': {
            'client': 'TechForward Agency',
            'year': '2024',
            'technologies': ['CSS Grid', 'Flexbox', 'SASS', 'Webpack'],
            'challenge': 'Deliver a pixel-perfect responsive design that works flawlessly across all devices and browsers.',
            'solution': 'Used modern CSS techniques, progressive enhancement, and extensive cross-browser testing.',
            'result': 'Achieved 100% Google Lighthouse scores across all metrics and 99.9% cross-browser compatibility.'
        }
    },
    {
        'id': 8,
        'title': 'Content Management System',
        'category': 'Backend Development',
        'description': 'A headless CMS solution providing flexible content management for multiple client websites.',
        'image': 'https://pixabay.com/get/g646be86bde7960733565b4ef465196b2ff1922b936767cbc06bc1e410da94010679c67c2e8e6ec07c2b066c6858fbf66ff98742a96bba58ed99257abc1b9c844_1280.jpg',
        'details': {
            'client': 'ContentFlow Systems',
            'year': '2023',
            'technologies': ['Node.js', 'GraphQL', 'MongoDB', 'Docker'],
            'challenge': 'Build a scalable CMS that can serve multiple websites while maintaining high performance.',
            'solution': 'Developed a microservices architecture with GraphQL API and automated deployment pipelines.',
            'result': 'Successfully serving 50+ websites with 99.9% uptime and reduced content update time by 80%.'
        }
    },
    {
        'id': 9,
        'title': 'Real Estate Platform',
        'category': 'Full Stack Development',
        'description': 'A comprehensive real estate platform with advanced search, virtual tours, and agent management.',
        'image': 'https://pixabay.com/get/g815dff5d92c477f17bb3847cc090145e1f406b9a88d393d7efb2cffda609c2171801641b68f12081de7d99f3e8319c23b9ee1a36e55a51d1574d58633d68e4db_1280.jpg',
        'details': {
            'client': 'PropertyHub Solutions',
            'year': '2024',
            'technologies': ['React', 'Express.js', 'PostgreSQL', 'AWS'],
            'challenge': 'Create a feature-rich platform that handles large property datasets and complex search queries.',
            'solution': 'Implemented elasticsearch for advanced search, image optimization, and real-time chat functionality.',
            'result': 'Processed over 100,000 property listings and facilitated $50M in real estate transactions.'
        }
    },
    {
        'id': 10,
        'title': 'Healthcare App Interface',
        'category': 'Mobile UI/UX',
        'description': 'A patient-focused healthcare app interface with appointment scheduling and health tracking.',
        'image': 'https://pixabay.com/get/g9e9fb4555a566a36d035d66ee47db33e3b21af3d8de9a07499b776fc15a9f14b1a992128299edc32643c997c8eaedba3b4207c614cae06bfa6ec9779765bc0c8_1280.jpg',
        'details': {
            'client': 'HealthConnect Medical',
            'year': '2024',
            'technologies': ['Flutter', 'Firebase', 'Dart', 'HL7 FHIR'],
            'challenge': 'Design a healthcare interface that prioritizes accessibility and HIPAA compliance.',
            'solution': 'Created an inclusive design with voice navigation, large text options, and end-to-end encryption.',
            'result': 'Improved patient engagement by 85% and received approval for use in 20+ medical facilities.'
        }
    },
    {
        'id': 11,
        'title': 'Data Visualization Platform',
        'category': 'Data Science',
        'description': 'An interactive data visualization platform for business intelligence and analytics reporting.',
        'image': 'https://pixabay.com/get/gc7b9c7b92bea4196c93279ef5aae127bd7dfa8523ea46281384bab2513b468bd17c8638a511634984d717c4d89bc4b7d9b7fade2fdc41079641a31aadf2078ee_1280.jpg',
        'details': {
            'client': 'DataInsight Analytics',
            'year': '2023',
            'technologies': ['Python', 'Plotly', 'Pandas', 'FastAPI'],
            'challenge': 'Build a platform that can handle large datasets while providing real-time interactive visualizations.',
            'solution': 'Implemented data streaming, caching strategies, and progressive data loading for optimal performance.',
            'result': 'Enabled analysis of 10TB+ datasets with sub-second response times and 95% user satisfaction.'
        }
    },
    {
        'id': 12,
        'title': 'Social Media Dashboard',
        'category': 'Digital Marketing',
        'description': 'A comprehensive social media management dashboard with scheduling and analytics features.',
        'image': 'https://pixabay.com/get/gceff48c7bdc4345cafdbf1d82dca45d3eba7aa9a25b19d5c7dc7906f7cc6de8439ff7b71144485c1745ddafd2b2b5c1772055e2c0e37fb639a9c59d66629b934_1280.jpg',
        'details': {
            'client': 'SocialFlow Marketing',
            'year': '2024',
            'technologies': ['Angular', 'Spring Boot', 'MySQL', 'OAuth'],
            'challenge': 'Integrate multiple social media APIs while maintaining user privacy and data security.',
            'solution': 'Built a secure API gateway with OAuth integration and automated content scheduling algorithms.',
            'result': 'Managed 1M+ social media posts and increased client engagement rates by 120%.'
        }
    },
    {
        'id': 13,
        'title': 'Creative Portfolio Showcase',
        'category': 'Creative Technology',
        'description': 'An innovative portfolio website featuring interactive animations and immersive user experiences.',
        'image': 'https://pixabay.com/get/ga34530cbd51c911e2618b6ae24aee2380d773af18b9dbe9587528a2dad0c417eb417b46cfc544772bf548d532945c7fe5d578aa1f75c36f081c4778966182a0a_1280.jpg',
        'details': {
            'client': 'Digital Artist Collective',
            'year': '2024',
            'technologies': ['Three.js', 'WebGL', 'GSAP', 'Canvas API'],
            'challenge': 'Create an immersive digital experience that showcases creative work without overwhelming the content.',
            'solution': 'Developed custom WebGL shaders and physics-based animations with progressive enhancement.',
            'result': 'Won 3 web design awards and increased portfolio views by 400% within the first month.'
        }
    }
]

def get_projects():
    """Get all projects"""
    return PROJECTS

def get_project_by_id(project_id):
    """Get a specific project by ID"""
    for project in PROJECTS:
        if project['id'] == project_id:
            return project
    return None

def get_projects_by_category(category):
    """Get projects filtered by category"""
    return [project for project in PROJECTS if project['category'] == category]

def get_featured_projects(limit=6):
    """Get featured projects for homepage"""
    return PROJECTS[:limit]
