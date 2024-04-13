<script lang="ts">
	enum Weight {
		Thin = 100,
		ExtraLight = 200,
		Light = 300,
		Regular = 400,
		Medium = 500,
		SemiBold = 600,
		Bold = 700,
		ExtraBold = 800,
		Black = 900
	}
	type FontStyle = 'normal' | 'italic';

	export let weight: Weight = Weight.Light;
	export let fontStyle: FontStyle = 'normal';
</script>

<span class="sans-serif" style="font-weight: {weight}; font-style: {fontStyle};">
	<slot />
</span>

<style>
	.sans-serif {
		font-family: 'Work Sans', sans-serif;
		font-optical-sizing: auto;
		font-style: normal;
	}
</style>
