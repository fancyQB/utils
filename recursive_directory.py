import os

all_file = []

def get_all_files(path):

	all_file_list = os.listdir(path)
	for file in all_file_list:
		file_path = os.path.join(path, file)
		if os.path.isdir(file_path):
			get_all_files(file_path)

		all_file.append(file_path)

	return all_file

#使用walk()函数
def getallfiles(path):

	for dirpath, dirname, filenames in os.walk(path):
		for dir in dirname:
			all_file.append(os.path.join(dirpath, dir))
		for name in filenames:
			all_file.append(os.path.join(dirpath, name))
	return all_file


if __name__ == '__main__':
	path = 'e:\资料'
	all_file = get_all_files(path)
	for item in all_file:
		print(item)