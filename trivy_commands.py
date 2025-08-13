import subprocess
import asyncio

async def run_trivy_scan(target: str, scan_type: str = "fs"):
    """
    Runs a Trivy scan on the specified target.
    
    Args:
        target (str): The target to scan (e.g., a directory path, image name).
        scan_type (str): The type of scan to perform (e.g., "fs" for filesystem, "image" for container image).
    """
    print(f"Running Trivy {scan_type} scan on: {target}")
    
    command = ["trivy", scan_type, target]
    
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    
    if stdout:
        print(f"Trivy Output:\n{stdout.decode()}")
    if stderr:
        print(f"Trivy Errors:\n{stderr.decode()}")
        
    if process.returncode == 0:
        print("Trivy scan completed successfully.")
    else:
        print(f"Trivy scan completed with errors (exit code: {process.returncode}).")

if __name__ == '__main__':
    # Example usage:
    # asyncio.run(run_trivy_scan(".", "fs"))
    # asyncio.run(run_trivy_scan("nginx:latest", "image"))
    pass
