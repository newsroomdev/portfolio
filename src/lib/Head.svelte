<script>
	export let title = "Gerald Rich's Portfolio";
	export let description = "Check out my portfolio and see what I've worked on.";
	export let keywords = 'portfolio, web development, front end, developer';
	export let author = 'Gerald Rich';
	export let image = 'https://example.com/image.png';
	export let url = 'https://example.com';
</script>

<svelte:head>
	<title>{title}</title>
	<link
		rel="stylesheet"
		href="https://s3.us-west-2.amazonaws.com/projects.geraldri.ch/css/bootstrap.min.css"
	/>
	<link
		rel="stylesheet"
		href="https://s3.us-west-2.amazonaws.com/projects.geraldri.ch/css/bootstrap-responsive.min.css"
	/>
	<meta name="description" content={description} />
	<meta name="keywords" content={keywords} />
	<meta name="author" content={author} />
	<meta property="og:type" content="website" />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:image" content={image} />
	<meta property="og:url" content={url} />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={description} />
	<meta name="twitter:image" content={image} />
	<meta name="twitter:url" content={url} />
	<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "{author}",
      "url": "{url}",
      "sameAs": [
        "https://www.linkedin.com/in/geraldrich/",
        "https://github.com/newsroomdev/",
        "https://twitter.com/newsroomdev/"
      ],
      "image": {
        "@type": "ImageObject",
        "url": "{image}",
        "height": "800",
        "width": "800"
      }
    }
	</script>
</svelte:head>
