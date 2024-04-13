// Squelch warnings of image imports from your assets dir
declare module '$lib/img/*' {
	let meta;
	export default meta;
}
