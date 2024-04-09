<script lang="ts">
	import { base } from '$app/paths';
	import type { Person, WithContext } from 'schema-dts';

	export let title = "Gerald Rich's Portfolio";
	export let description = "A few things I've worked on.";
	export let keywords = 'portfolio, web development, front end, developer, journalism';
	export let author = 'Gerald Rich';
	export let url = base;

	const schemaObj: WithContext<Person> = {
		'@context': 'https://schema.org',
		'@type': 'Person',
		name: '{author}',
		url: '{url}',
		sameAs: [
			'https://www.linkedin.com/in/geraldrich/',
			'https://github.com/newsroomdev/',
			'https://twitter.com/newsroomdev/'
		],
		hasOccupation: {
			'@type': 'Occupation',
			name: 'Interactive News Editor, AP'
		}
	};
	const jsonLD = `
    <script type="application/ld+json">
      ${JSON.stringify(schemaObj)}
    ${'<'}/script>
  `;
</script>

<svelte:head>
	<title>{title}</title>
	<link
		rel="stylesheet"
		href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
		integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
		crossorigin="anonymous"
	/>
	<meta name="description" content={description} />
	<meta name="keywords" content={keywords} />
	<meta name="author" content={author} />
	<meta property="og:type" content="website" />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:url" content={url} />
	<meta name="twitter:card" content="summary" />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={description} />
	<meta name="twitter:url" content={url} />
	{@html jsonLD}
</svelte:head>
