import sys
import argparse
import os
import csv
import yaml


def writeYmlFile(file_path : str, obj : dict) -> None:
    with open(file_path, 'w') as outfile:
        yaml.dump(obj, outfile, default_flow_style=False, sort_keys=False)


def generate_yml_files(csv_file_path, output_folder):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count = line_count + 1
                continue
            line_count = line_count + 1
            yaml_data = dict()
            yaml_data["Name"] = row[0]
            yaml_data["Author"] = row[1]
            yaml_data["Created"] = row[2]
            commands_data = dict()
            commands_data["Command"] = row[4]
            commands_data["Description"] = row[5]
            commands_data["Usecase"] = row[6]
            commands_data["Category"] = row[7]
            commands_data["Privileges"] = row[8]
            commands_data["MitreID"] = row[9]
            commands_data["OperatingSystem"] = row[10]
            yaml_data["Commands"] = commands_data
            yaml_data["Resources"] = [row[11][6:]]
            yaml_data["driver_description"] = row[12]
            acknowledgement_data = dict()
            acknowledgement_data["Person"] = row[14]
            acknowledgement_data["Handle"] = row[15]
            yaml_data["Acknowledgement"] = acknowledgement_data
            detection_data = list()
            for detection in row[16].split(", "):
                if detection.startswith("IOC"):
                    detection_data.append({
                        "type": 'IOC',
                        "value": detection[5:]
                    })
                elif detection.startswith("BlockRule"):
                    detection_data.append({
                        "type": 'BlockRule',
                        "value": detection[11:]
                    })    
            yaml_data["Detection"] = detection_data
            yaml_data["KnownHashes"] = row[17]
            metadata = dict()
            metadata["binary"] = row[19]
            metadata["Verified"] = row[20]
            metadata["Date"] = row[21]
            metadata["Publisher"] = row[22]
            metadata["Company"] = row[23]
            metadata["Description"] = row[24]
            metadata["Product"] = row[25]
            metadata["ProductVersion"] = row[26]
            metadata["FileVersion"] = row[27]
            metadata["MachineType"] = row[28]
            metadata["OriginalFilename"] = row[29]
            yaml_data["Metadata"] = metadata

            file_name = os.path.splitext(yaml_data["Name"])[0] + '.yaml'
            writeYmlFile(os.path.join('yaml/' + output_folder, file_name), yaml_data)               


def generate(args):
    generate_yml_files(args.input, args.output)


def main(args):
    print("test")
    parser = argparse.ArgumentParser(
    description="loldriver yaml file generator")
    parser.add_argument("-i", "--input", required=False, default="drivers.csv",
                        help="input csv file containing drivers.csv data")
    parser.add_argument("-o", "--output", required=False, default=".",
                        help="output folder")

    parser.set_defaults(func=generate)

    args = parser.parse_args()
    
    return args.func(args)

if __name__ == "__main__":
    main(sys.argv[1:])
