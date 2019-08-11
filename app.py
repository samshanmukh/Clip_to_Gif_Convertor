"""clip to gif convertor app [main file]."""
import imageio
import os

clip = os.path.abspath('lightning02.mp4')

def gifMaker(inputPath, targetFormat):
	outputPath = os.path.splitext(inputPath)[0] + targetFormat

	print(f'converting {inputPath} \n to {outputPath}')

	reader = imageio.get_reader(inputPath)

	fps = reader.get_meta_data()['fps']

	writer = imageioe.get_writer(outputPath, fps = fps)

	for frame in reader:
		writer.append_data(frame)
		print(f'Frame {frame}')

	print('Successfully converted')
	writer.close()

gifMaker(clip, '.gif')