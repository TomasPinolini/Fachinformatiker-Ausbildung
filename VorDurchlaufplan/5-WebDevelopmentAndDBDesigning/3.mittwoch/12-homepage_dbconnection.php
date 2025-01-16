<!-- Task: Apply Bootstrap styling to the homepage with a navigation bar
Instructions: This file uses Bootstrap for styling the homepage and navigation bar. -->

<!DOCTYPE html>
<html>
<head>
    <title>Homepage</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">My Website</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#services">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-5">
        <section id="welcome" class="mb-5">
            <h1 class="text-center">Welcome to the Homepage</h1>
            <p class="text-center">This is the main page of the website. Navigate using the menu above.</p>
        </section>

        <!-- About Section -->
        <section id="about" class="mb-5">
            <h2>About Us</h2>
            <p>Learn more about our mission and values.</p>
        </section>

        <!-- Services Section -->
        <section id="services" class="mb-5">
            <h2>Our Services</h2>
            <p>Discover the services we offer to help you succeed.</p>
        </section>

        <!-- Contact Section -->
        <section id="contact">
            <h2>Contact Us</h2>
            <p>Get in touch with us for more information.</p>
        </section>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
