import os

def is_code(filename):
	if filename[-5:] == ".java": return True
	if filename[-3:] == ".py": return True
	if filename[-4:] == ".cpp": return True
	if filename[-3:] == ".sh": return True
	return False

def get_urls_local(base_dir):
	for item in os.listdir(base_dir):
		if os.path.isfile(base_dir + "/" + item):
			yield base_dir + "/" + item
		elif os.path.isdir(base_dir + "/" + item):
			for sub_item in get_urls_local(base_dir + "/" + item):
				yield sub_item

def aggregate(base_dir, dest):
	destination_file = open(dest, "w+")
	for item in list(get_urls_local(base_dir)):
		if is_code(item):
			source = open(item, "rb").read()
			destination_file.write("-------- %s -------------\n" % item)
			destination_file.write(source)

if __name__ == "__main__":
	aggregate("/Users/calpeyser/Desktop/bazel/", "/Users/calpeyser/Desktop/code.txt")
