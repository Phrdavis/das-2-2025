import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_s3_bucket(bucket_name, region=None):
    try:
        # Cria o cliente S3
        s3_client = boto3.client('s3', region_name=region)

        # Cria o bucket
        if region:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        else:
            s3_client.create_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' criado com sucesso!")
    except NoCredentialsError:
        print("Erro: Credenciais da AWS não encontradas.")
    except PartialCredentialsError:
        print("Erro: Credenciais da AWS incompletas.")
    except Exception as e:
        print(f"Erro ao criar o bucket: {e}")

# Exemplo de uso
if __name__ == "__main__":
    bucket_name = "davi270402"
    region = "sa-east-1"  # Substitua pela região desejada, ou deixe como None para usar a região padrão
    create_s3_bucket(bucket_name, region)