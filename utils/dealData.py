import numpy as np
import os

databasesName = ["ship_dataset.npy", "rechange_val_data_plane_Radar.npy"]


def dealSkeleton(file):
    def read_xyz(file, max_body=2, num_joint=25):
        seq_info = read_skeleton(file)
        data = np.zeros((3, seq_info["numFrame"], num_joint, max_body))
        for n, f in enumerate(seq_info["frameInfo"]):
            for m, b in enumerate(f["bodyInfo"]):
                for j, v in enumerate(b["jointInfo"]):
                    if m < max_body and j < num_joint:
                        data[:, n, j, m] = [v["x"], v["y"], v["z"]]
                    else:
                        pass
        return data

    def read_skeleton(file):
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            skeleton_sequence = {}
            skeleton_sequence["numFrame"] = int(f.readline())
            skeleton_sequence["frameInfo"] = []
            for t in range(skeleton_sequence["numFrame"]):
                frame_info = {}
                frame_info["numBody"] = int(f.readline())
                frame_info["bodyInfo"] = []
                for m in range(frame_info["numBody"]):
                    body_info = {}
                    body_info_key = [
                        "bodyID",
                        "clipedEdges",
                        "handLeftConfidence",
                        "handLeftState",
                        "handRightConfidence",
                        "handRightState",
                        "isResticted",
                        "leanX",
                        "leanY",
                        "trackingState",
                    ]
                    body_info = {
                        k: float(v) for k, v in zip(body_info_key, f.readline().split())
                    }
                    body_info["numJoint"] = int(f.readline())
                    body_info["jointInfo"] = []
                    for v in range(body_info["numJoint"]):
                        joint_info_key = [
                            "x",
                            "y",
                            "z",
                            "depthX",
                            "depthY",
                            "colorX",
                            "colorY",
                            "orientationW",
                            "orientationX",
                            "orientationY",
                            "orientationZ",
                            "trackingState",
                        ]
                        joint_info = {
                            k: float(v)
                            for k, v in zip(joint_info_key, f.readline().split())
                        }
                        body_info["jointInfo"].append(joint_info)
                    frame_info["bodyInfo"].append(body_info)
                skeleton_sequence["frameInfo"].append(frame_info)
        return skeleton_sequence

    def get_links():
        neighbor_1base = [
            (1, 2),
            (2, 21),
            (3, 21),
            (4, 3),
            (5, 21),
            (6, 5),
            (7, 6),
            (8, 7),
            (9, 21),
            (10, 9),
            (11, 10),
            (12, 11),
            (13, 1),
            (14, 13),
            (15, 14),
            (16, 15),
            (17, 1),
            (18, 17),
            (19, 18),
            (20, 19),
            (22, 23),
            (23, 8),
            (24, 25),
            (25, 12),
        ]
        neighbor_link = [(i - 1, j - 1) for (i, j) in neighbor_1base]
        return neighbor_link

    datas = {}
    points = read_xyz(file)
    points = points[:, :, :, 0]
    points = np.transpose(points, [1, 2, 0])
    points[:, :, [0, 1, 2]] = points[:, :, [2, 0, 1]]
    points[:, :, 0] -= np.median(points[:, :, 0])
    points[:, :, 2] += np.abs(np.min(points[:, :, 2]))

    datas["points"] = points
    datas["links"] = get_links()
    return datas


def dealNpy(file):
    if os.path.basename(file) == "ship_dataset.npy":
        # 读取 ship_dataset.npy 文件
        samples_array = np.load(file)

        # 初始化 datas 字典
        datas = {"points": None, "lines": []}

        # 提取帧数、点数和坐标维度
        num_samples, XYZcoordinat, frames, num_points, _ = samples_array.shape
        # print(samples_array.shape)
        # 将 samples_array 转换为所需的形状 [frames, num_points, XYZcoordinate]
        datas["points"] = samples_array[0, :, :, :, 0]
        datas["points"] = np.transpose(datas["points"], (1, 2, 0))
        # print(datas["points"].shape)
        # 获取经度和纬度的最大值和最小值
        longitudes = datas["points"][:, :, 0]
        latitudes = datas["points"][:, :, 1]

        min_longitude = longitudes.min()
        max_longitude = longitudes.max()
        min_latitude = latitudes.min()
        max_latitude = latitudes.max()

        # 对经纬度进行归一化
        datas["points"][:, :, 0] = (longitudes - min_longitude) / (
            max_longitude - min_longitude
        )
        datas["points"][:, :, 1] = (latitudes - min_latitude) / (
            max_latitude - min_latitude
        )

        # 提取轨迹数据
        for num_point in range(num_points):
            # 提取当前帧的所有点
            points = datas["points"][:, num_point, :]
            datas["lines"].append(points)
        return datas

    elif os.path.basename(file) == "rechange_val_data_plane_Radar.npy":
        # 读取 rechange_val_data_plane_Radar.npy 文件
        real = {}
        data = (np.load(file)[0])[0:3]
        data = data.transpose(1, 2, 0, 3)
        data = data.squeeze()
        for i in range(3):
            temp = np.max(data[:, :, i]) - np.min(data[:, :, i])
            data[:, :, i] = (data[:, :, i] - np.min(data[:, :, i])) / temp * 3
        # print(data.shape)
        real["points"] = data
        print(real["points"].shape)
        line1 = data[:, 0, :]
        line2 = data[:, 1, :]
        lines = [line1, line2]
        real["lines"] = lines

        return real


def getSamplesLength(filePath):
    if filePath is None:
        return None
    if os.path.basename(filePath) == "ship_dataset.npy":
        # 读取 ship_dataset.npy 文件
        samples_array = np.load(filePath)

        # 提取帧数、点数和坐标维度
        num_samples, XYZcoordinat, frames, num_points, _ = samples_array.shape
        return num_samples
    elif os.path.basename(filePath) == "rechange_val_data_plane_Radar.npy":
        # 读取 rechange_val_data_plane_Radar.npy 文件
        num_samples = (np.load(filePath)).shape[0]
        return num_samples
    elif os.path.basename(filePath) == "five_planes.npy":
        # 读取 five_planes.npy 文件
        num_samples = (np.load(filePath)).shape[0]
        return num_samples
    elif os.path.splitext(filePath)[1] == ".skeleton":
        return 0
    else:
        return None


def getSampleDatas(datasetPath, index):
    if os.path.basename(datasetPath) == "ship_dataset.npy":
        try:
            # 读取 ship_dataset.npy 文件
            samples_array = np.load(datasetPath)

            # 初始化 datas 字典
            datas = {"points": None, "lines": []}

            # 提取帧数、点数和坐标维度
            num_samples, XYZcoordinat, frames, num_points, _ = samples_array.shape
            # print(samples_array.shape)
            # 将 samples_array 转换为所需的形状 [frames, num_points, XYZcoordinate]
            datas["points"] = samples_array[index, :, :, :, 0]
            datas["points"] = np.transpose(datas["points"], (1, 2, 0))
            # print(datas["points"].shape)
            # 获取经度和纬度的最大值和最小值
            longitudes = datas["points"][:, :, 0]
            latitudes = datas["points"][:, :, 1]

            min_longitude = longitudes.min()
            max_longitude = longitudes.max()
            min_latitude = latitudes.min()
            max_latitude = latitudes.max()

            # 对经纬度进行归一化
            datas["points"][:, :, 0] = (longitudes - min_longitude) / (
                max_longitude - min_longitude
            )
            datas["points"][:, :, 1] = (latitudes - min_latitude) / (
                max_latitude - min_latitude
            )

            # 提取轨迹数据
            for num_point in range(num_points):
                # 提取当前帧的所有点
                points = datas["points"][:, num_point, :]
                datas["lines"].append(points)
            return datas
        except:
            print("读取ship_dataset.npy失败！")

    elif os.path.basename(datasetPath) == "rechange_val_data_plane_Radar.npy":
        try:
            # 读取 rechange_val_data_plane_Radar.npy 文件
            real = {}
            data = (np.load(datasetPath)[index])[0:3]
            data = data.transpose(1, 2, 0, 3)
            data = data.squeeze()
            data = data[(np.sum(data != 0, axis=2)) == 3].reshape(-1, 2, 3)
            for i in range(3):
                temp = np.max(data[:, :, i]) - np.min(data[:, :, i])
                data[:, :, i] = (data[:, :, i] - np.min(data[:, :, i])) / temp * 2
            # print(data.shape)
            real["points"] = data
            # print(real["points"].shape)
            lines = []
            for n in range(data.shape[1]):
                lines.append(data[:, n, :])
            real["lines"] = lines

            return real
        except:
            print("读取rechange_val_data_plane_Radar.npy失败！")

    elif os.path.basename(datasetPath) == "five_planes.npy":
        try:
            # 读取 five_planes.npy 文件
            real = {}
            data = np.load(datasetPath)[index]
            data = data.transpose(1, 2, 0, 3)
            data = data.squeeze()
            for i in range(3):
                temp = np.max(data[:, :, i]) - np.min(data[:, :, i])
                data[:, :, i] = (data[:, :, i] - np.min(data[:, :, i])) / temp * 2
            # print(data.shape)
            real["points"] = data
            # print(real["points"].shape)
            lines = []
            for n in range(data.shape[1]):
                lines.append(data[:, n, :])
            real["lines"] = lines

            return real
        except:
            print("读取five_planes.npy失败！")
    elif os.path.splitext(datasetPath)[1] == ".skeleton":  # Skeleton的骨架数据
        try:
            return dealSkeleton(datasetPath)
        except:
            print("读取skeleton文件失败！")
    # 可正常读取的方法全部失败，返回None
    return None


if __name__ == "__main__":
    datas = getSampleDatas(".//datas//rechange_val_data_plane_Radar.npy", 5)
