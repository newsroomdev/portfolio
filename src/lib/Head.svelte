<script lang="ts">
	import { base } from '$app/paths';
	import type { Person, WithContext } from 'schema-dts';

	export let title = "Gerald Rich's Portfolio";
	export let description = "A few things I've worked on.";
	export let keywords = 'portfolio, web development, front end, developer, journalism';
	export let author = 'Gerald Rich';

	const schemaObj: WithContext<Person> = {
		'@context': 'https://schema.org',
		'@type': 'Person',
		name: '{author}',
		url: '{base}',
		sameAs: [
			'https://www.linkedin.com/in/geraldrich/',
			'https://github.com/newsroomdev/',
			'https://twitter.com/newsroomdev/'
		],
		hasOccupation: {
			'@type': 'Occupation',
			name: 'Newsroom Developer Consultant'
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
	<meta name="description" content={description} />
	<meta name="keywords" content={keywords} />
	<meta name="author" content={author} />
	<meta property="og:type" content="website" />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:url" content={base} />
	<meta name="twitter:card" content="summary" />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={description} />
	<meta name="twitter:url" content={base} />
	{@html jsonLD}
	<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin="anonymous" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,100..900;1,100..900&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap"
		rel="stylesheet"
	/>
</svelte:head>
