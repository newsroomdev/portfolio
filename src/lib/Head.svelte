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
	<style>
		/* cyrillic-ext */
		@font-face {
			font-family: 'Bitter';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax-HiqOu8IVPmn7erxmJD1wmULYyT8.woff2)
				format('woff2');
			unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
		}
		/* cyrillic */
		@font-face {
			font-family: 'Bitter';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax-HiqOu8IVPmn7erxvJD1wmULYyT8.woff2)
				format('woff2');
			unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
		}
		/* vietnamese */
		@font-face {
			font-family: 'Bitter';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax-HiqOu8IVPmn7erxkJD1wmULYyT8.woff2)
				format('woff2');
			unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0,
				U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
		}
		/* latin-ext */
		@font-face {
			font-family: 'Bitter';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax-HiqOu8IVPmn7erxlJD1wmULYyT8.woff2)
				format('woff2');
			unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
				U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
		}
		/* latin */
		@font-face {
			font-family: 'Bitter';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax-HiqOu8IVPmn7erxrJD1wmULY.woff2)
				format('woff2');
			unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304,
				U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF,
				U+FFFD;
		}
		/* cyrillic-ext */
		@font-face {
			font-family: 'Bitter';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax8HiqOu8IVPmn7coxpLjpSm3LZ.woff2)
				format('woff2');
			unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
		}
		/* cyrillic */
		@font-face {
			font-family: 'Bitter';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax8HiqOu8IVPmn7e4xpLjpSm3LZ.woff2)
				format('woff2');
			unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
		}
		/* vietnamese */
		@font-face {
			font-family: 'Bitter';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax8HiqOu8IVPmn7cIxpLjpSm3LZ.woff2)
				format('woff2');
			unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0,
				U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
		}
		/* latin-ext */
		@font-face {
			font-family: 'Bitter';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax8HiqOu8IVPmn7cYxpLjpSm3LZ.woff2)
				format('woff2');
			unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
				U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
		}
		/* latin */
		@font-face {
			font-family: 'Bitter';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/bitter/v33/rax8HiqOu8IVPmn7f4xpLjpSmw.woff2)
				format('woff2');
			unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304,
				U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF,
				U+FFFD;
		}
		/* vietnamese */
		@font-face {
			font-family: 'Work Sans';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/worksans/v19/QGYqz_wNahGAdqQ43Rh_eZDkv_1i4_D2E4A.woff2)
				format('woff2');
			unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0,
				U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
		}
		/* latin-ext */
		@font-face {
			font-family: 'Work Sans';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/worksans/v19/QGYqz_wNahGAdqQ43Rh_eZDlv_1i4_D2E4A.woff2)
				format('woff2');
			unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
				U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
		}
		/* latin */
		@font-face {
			font-family: 'Work Sans';
			font-style: italic;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/worksans/v19/QGYqz_wNahGAdqQ43Rh_eZDrv_1i4_D2.woff2)
				format('woff2');
			unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304,
				U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF,
				U+FFFD;
		}
		/* vietnamese */
		@font-face {
			font-family: 'Work Sans';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/worksans/v19/QGYsz_wNahGAdqQ43Rh_c6DptfpA4cD3.woff2)
				format('woff2');
			unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0,
				U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;
		}
		/* latin-ext */
		@font-face {
			font-family: 'Work Sans';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/worksans/v19/QGYsz_wNahGAdqQ43Rh_cqDptfpA4cD3.woff2)
				format('woff2');
			unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
				U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
		}
		/* latin */
		@font-face {
			font-family: 'Work Sans';
			font-style: normal;
			font-weight: 100 900;
			font-display: swap;
			src: url(https://fonts.gstatic.com/s/worksans/v19/QGYsz_wNahGAdqQ43Rh_fKDptfpA4Q.woff2)
				format('woff2');
			unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304,
				U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF,
				U+FFFD;
		}
	</style>
</svelte:head>
