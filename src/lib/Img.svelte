<script lang="ts">
	export let img: string;
	export let alt: string;
	export let loading: string = 'lazy';
	const modules = import.meta.glob('$lib/img/*.{avif,gif,heif,jpeg,jpg,png,tiff,webp}', {
		import: 'default',
		eager: true,
		query: { w: 780, enhanced: true }
	});
	let src = Object.entries(modules)
		.filter(([key, value]) => key.includes(img))
		.map((i) => i[1] as string)[0];

	const sizes = [
		'(min-width: 1440px) 320px',
		'(min-width: 1024px) 40vw',
		'(min-width: 768px) 45vw',
		'(max-width: 425px) 90vw',
		'380px'
	];
	const imgSizes = sizes.join(', ');
</script>

{#if src}
	<enhanced:img {src} {loading} {alt} sizes={imgSizes} />
{:else}
	<p style="color:red;">Image not found</p>
{/if}
