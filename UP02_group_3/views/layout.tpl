<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Math Solver</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/style.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="next">
        <div style="display:flex;flex-direction:column;height:100vh">
            <header>
                <div class="page-header">
                    <div class="phc">
                        <div class="pagelogos">
                            <a href="/" class="headerlogotext">
                                <img alt="Math Solver" src="static\images\logo.png" class="headerlogo">
                                <span class="headertext">Math Solver</span>
                            </a>
                        </div>
                        <div>
                            <a href="/home" class="headerlink">
                            <span>Главная</span>
                        </a>
                        <a href="/authors" class="headerlink">
                            <span>Об авторах</span>
                        </a>
                        </div>
                    </div>
                </div>
            </header>

            <div class="page-layout-container">
                {{!base}}
            </div>

            <footer class="SiteFooter">
                <div class="container">
                    <div class="content">
                        <ul>
                            <li><a href="/authors">О нас</a></li>
                            <li>@Math Solver 2023</li>
                        </ul>
                    </div>
                </div>
            </footer>
        </div>
    </div>
    
    <script src="/static/scripts/plotting.js"</script>
    <script src="/static/scripts/reading.js"</script>
    <script src="/static/scripts/imganim.js"</script>
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
</body>
</html>
