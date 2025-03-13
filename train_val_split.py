import os
import shutil
import random
import argparse


def split_dataset(data_dir, ratio=0.8, seed=None):
    # 设置随机种子
    random.seed(seed)

    # 支持的图片格式（不区分大小写）
    img_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

    # 获取所有图片文件
    files = []
    for f in os.listdir(data_dir):
        file_path = os.path.join(data_dir, f)
        if os.path.isfile(file_path):
            ext = os.path.splitext(f)[1].lower()
            if ext in img_exts:
                files.append(f)

    if not files:
        raise ValueError(f"No image files found in {data_dir}")

    # 打乱文件顺序
    random.shuffle(files)

    # 计算划分点
    split_idx = int(len(files) * ratio)
    train_files = files[:split_idx]
    val_files = files[split_idx:]

    # 创建输出目录
    parent_dir = os.path.dirname(data_dir)
    folder_name = os.path.basename(data_dir.rstrip(os.sep))

    train_dir = os.path.join(parent_dir, f"{folder_name}_test")
    val_dir = os.path.join(parent_dir, f"{folder_name}_val")

    # 检查目录是否存在
    for d in [train_dir, val_dir]:
        if os.path.exists(d):
            raise FileExistsError(f"Directory {d} already exists. Please remove it first.")
        os.makedirs(d)

    # 复制文件函数
    def copy_files(files, dest_dir):
        for f in files:
            src = os.path.join(data_dir, f)
            dst = os.path.join(dest_dir, f)
            shutil.copy2(src, dst)  # 保留文件元数据

    # 执行复制
    copy_files(train_files, train_dir)
    copy_files(val_files, val_dir)

    return len(train_files), len(val_files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="划分图片数据集")
    parser.add_argument("--data_dir", type=str, required=True,
                        help="包含图片的原始目录路径")
    parser.add_argument("--ratio", type=float, default=0.8,
                        help="训练集划分比例（0-1），默认0.8")
    parser.add_argument("--seed", type=int, default=None,
                        help="随机种子（可选）")

    args = parser.parse_args()

    try:
        train_count, val_count = split_dataset(
            data_dir=args.data_dir,
            ratio=args.ratio,
            seed=args.seed
        )
        print(f"划分完成！训练集 {train_count} 张，验证集 {val_count} 张")
        print(f"训练集路径：{os.path.dirname(args.data_dir)}/{os.path.basename(args.data_dir.rstrip(os.sep))}_test")
        print(f"验证集路径：{os.path.dirname(args.data_dir)}/{os.path.basename(args.data_dir.rstrip(os.sep))}_val")
    except Exception as e:
        print(f"错误发生：{str(e)}")