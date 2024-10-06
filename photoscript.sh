#Directories
## Daniel Upploads
upload_daniel=(
	"/home/main/PhotoMount/SharedFolders/Daniel-All"
	"/home/main/PhotoMount/SharedFolders/Daniel-Vernersson"
	"/home/main/PhotoMount/SharedFolders/Daniel-Mattsson"
)


display_tablet_vasa='/home/main/PhotoMount/Tablets/TabletVasa'

rm -rf "$display_tablet_vasa/*"

for upload_dir in "${upload_daniel[@]}"; do
	echo "Processing Folder: $upload_dir"

	# Find photos less than 1 week old. 
	find "$upload_dir" -type f -mtime -7 \( -name "*.jpg" -o -name "*.png" \) |  while read file; do
		cp "$file" "$display_tablet_vasa/"
		echo "Added $file to tablet folder $display_tablet_vasa"
	done
done


echo "Total Photos in Display Folder is $(find "$display_dir" -type f \( -name "*.jpg" -o -name "*.png" \) | wc -l)"

	

