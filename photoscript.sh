#Directories
## Daniel Upploads
upload_daniel=(
	"/home/main/PhotoMount/SharedFolders/Daniel-All"
	"/home/main/PhotoMount/SharedFolders/Daniel-Vernersson"
	"/home/main/PhotoMount/SharedFolders/Daniel-Mattsson"
)


display_tablet_vasa="/home/main/PhotoMount/Tablets/VasaTablet"

rm -rf "/home/main/PhotoMount/Tablets/VasaTablet/*"


display_amount_goal=300

for upload_dir in "${upload_daniel[@]}"; do
	echo "Processing Folder: $upload_dir"

	# Find photos less than 24 hours old. 
	find "$upload_dir" -type f -mtime -1 \( -name "*.jpg" -o -name "*.png" \) |  while read file; do
		#Looks for meta data to see when photo was taken
		photo_date=$(exiftool -DateTimeOriginal -d "%Y-%m-%d" "$file" | awk -F ': ' '{print $2}')
		#Checks if photo_date is set, if not set the it sets photo date to retrieve modified date instead.
		if [ -z "$photo_date" ]; then
			photo_date=$(stat --format="%y" "$file" | cut -d'' -f1)
		fi
		recent_limit=7
		if [[ $(date -d "$photo_date" +%s) -ge $(date -d "$current_date - $recent_limit days" +%s) ]]; then
			cp "$file" "$display_tablet_vasa/"
			echo "Added $file to tablet folder $display_tablet_vasa due to recent"
		fi
	done
done

image_count_first_check=$(find "$display_tablet_vasa" -type f \( -name "*.jpg" -o -name "*.png" \) | wc -l)
if [ "$image_count_first_check" -lt "$display_amount_goal" ]; then
	echo "Not enough new images, filling display folder with anneversaries..."
	fill=$(("$display_amount_goal" - "$image_count_first_check"))


	for upload_dir in "${upload_daniel[@]}"; do
		find "$upload_dir" -type f \( -name "*.jpg" -o -name "*.png" \) | shuf -n "$fill" | while read file; do
		
			#Looks for meta data to see when photo was taken
			photo_date=$(exiftool -DateTimeOriginal -d "%Y-%m-%d" "$file" | awk -F ': ' '{print $2}')
			#Checks if photo_date is set, if not set the it sets photo date to retrieve modified date instead.
			if [ -z "$photo_date" ]; then
				photo_date_ann=$(stat --format="%y" "$file" | cut -d'' -f2-3)
			fi
			recent_limit=7
			if [[ $(date -d "$photo_date" +%s) -ge $(date -d "$current_date - $recent_limit days" +%s) ]]; then
				cp "$file" "$display_tablet_vasa/"
				echo "Added $file to tablet folder $display_tablet_vasa due to recent"
			fi
		
		cp "$file" "$display_tablet_vasa"
		echo "Added $file to to $display_tablet_vasa, filling..."
	done
done
fi



image_count=$(find "$display_tablet_vasa" -type f \( -name "*.jpg" -o -name "*.png" \) | wc -l)
if [ "$image_count" -lt 100 ]; then
	echo "Fewer than 100 images, filling display folder..."
	fill=$((100 - image_count))


	for upload_dir in "${upload_daniel[@]}"; do
		find "$upload_dir" -type f \( -name "*.jpg" -o -name "*.png" \) | shuf -n "$fill" | while read file; do
		cp "$file" "$display_tablet_vasa"
		echo "Added $file to to $display_tablet_vasa, filling..."
	done
done
fi

echo "Total Photos in Display Folder is $(find "$display_tablet_vasa" -type f \( -name "*.jpg" -o -name "*.png" \) | wc -l)"

	

