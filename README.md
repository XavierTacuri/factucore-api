# FactuCore Backend

Backend FastAPI generado como punto de partida para migrar la base legacy `sistema_ee`.

Este proyecto mantiene los nombres originales de tablas y columnas para poder conectarse a la
base legacy actual sin alterar el sistema Java. La normalizacion de nombres, tipos monetarios y
claves foraneas debe hacerse con migraciones Alembic controladas.

## Ejecutar

```powershell
cd "C:\Users\ZenBook\Desktop\FactuCore API\factucore_backend"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
copy .env.example .env
docker compose up -d postgres
uvicorn app.main:app --reload
```

## Modulos iniciales

- Clientes
- Usuarios
- Catalogos: categorias, marcas, impuestos, almacenes
- Articulos e inventario
- Facturas y detalles
- Creditos y depositos
- Proformas
- Ordenes de trabajo
- Proveedores y compras

## Siguientes pasos recomendados

1. Adaptar y cargar `database/BDD20221130.sql` en PostgreSQL.
2. Configurar `DATABASE_URL` para PostgreSQL.
3. Validar datos huerfanos antes de activar nuevas FK.
4. Crear migraciones Alembic para convertir dinero de `DOUBLE` a `DECIMAL`.
5. Migrar contrasenas de `usuario.userClave` a hashes seguros.
