import { readdir, writeFile } from 'fs';
import { dirname, join, basename } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const dir = join(__dirname, '../src/lib/img');

readdir(dir, (err, files) => {
	if (err) {
		console.error(`Error reading directory: ${err}`);
		process.exit(1);
	}

	const baseNames = files
		.filter((file) => !file.startsWith('.'))
		.filter((file) => !file.endsWith('txt'))
		.map((file) => basename(file));

	const filePath = join(__dirname, '../src/lib/img/index.txt');
	writeFile(filePath, baseNames.join('\n'), (err) => {
		if (err) {
			console.error(`Error writing file: ${err}`);
			process.exit(1);
		}
	});
});
