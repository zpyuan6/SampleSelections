import random
import json
import os

def random_selection(
    dataset_folder,
    target_number):

    dataset_annotation = json.load(open(os.path.join(dataset_folder, 'final_flickr_separateGT_train.json'), 'r'))

    image_items = dataset_annotation['images']

    annoatations = dataset_annotation['annotations']

    old_image_list = set([items['file_name'] for items in image_items])

    new_image_list = random.sample(old_image_list, target_number)

    new_image_items = []
    new_image_id = []

    for items in image_items:
        if items['file_name'] in new_image_list:
            new_image_items.append(items)
            new_image_id.append(items['id'])

    new_annotations = []

    for ann in annoatations:
        if ann['image_id'] in new_image_id:
            new_annotations.append(ann)

    print(dataset_annotation)

    new_json_annotation_file = dataset_annotation

    new_json_annotation_file['images'] = new_image_items
    new_json_annotation_file['annotations'] = new_annotations

    with open(os.path.join(dataset_folder, f'final_flickr_separateGT_train_random_{str(target_number)}.json'), 'w') as f:
        json.dump(new_json_annotation_file, f)



if __name__ == "__main__":

    dataset_folder = "X:\\pervasive_group\\Shared\\flickr30k"

    target_number = 3000

    random_selection(dataset_folder, target_number)

