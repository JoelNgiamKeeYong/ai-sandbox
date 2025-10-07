import torch
import platform
import psutil


class TorchInfo:
    """Utility class for inspecting PyTorch, CUDA, GPU, and system info."""

    @staticmethod
    def print_torch_info():
        print("=== PyTorch & CUDA Info ===")
        print(f"Torch version        : {torch.__version__}")
        print(f"CUDA available       : {torch.cuda.is_available()}")
        print(f"CUDA version         : {torch.version.cuda}")
        print(f"CUDNN version        : {torch.backends.cudnn.version() if torch.backends.cudnn.is_available() else 'N/A'}")
        print(f"Number of GPUs       : {torch.cuda.device_count()}")
        print()

    @staticmethod
    def print_gpu_info():
        if not torch.cuda.is_available():
            print("⚠️  No GPU detected. Using CPU only.")
            return

        print("=== GPU Info ===")
        for i in range(torch.cuda.device_count()):
            props = torch.cuda.get_device_properties(i)
            print(f"GPU {i} - {torch.cuda.get_device_name(i)}")
            print(f"  - Compute Capability : {props.major}.{props.minor}")
            print(f"  - Total Memory       : {props.total_memory / 1024 ** 3:.2f} GB")
            print(f"  - Allocated Memory   : {torch.cuda.memory_allocated(i) / 1024 ** 2:.2f} MB")
            print(f"  - Reserved Memory    : {torch.cuda.memory_reserved(i) / 1024 ** 2:.2f} MB")
            print(f"  - MultiProcessor Cnt : {props.multi_processor_count}")
            print()

    @staticmethod
    def print_system_info():
        print("=== System Info ===")
        print(f"OS              : {platform.system()} {platform.release()}")
        print(f"OS Version      : {platform.version()}")
        print(f"Machine         : {platform.machine()}")
        print(f"Processor       : {platform.processor()}")
        print(f"CPU Cores       : {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
        print(f"Total RAM       : {psutil.virtual_memory().total / 1024 ** 3:.2f} GB")
        print()

    @classmethod
    def print_all(cls):
        """Print all available info."""
        cls.print_torch_info()
        cls.print_gpu_info()
        cls.print_system_info()


# Example usage
if __name__ == "__main__":
    TorchInfo.print_all()
