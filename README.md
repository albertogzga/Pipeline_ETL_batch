# Pipeline_ETL_batch
Pipeline que extrae datos de un archivo CSV
graph LR
    A[Fuente de Datos CSV] -->|Extract: pandas| B(Transform: Limpieza y Normalización)
    B -->|Load: DDL & to_sql| C[(Base de Datos SQL)]
    C -->|Análisis| D[Consultas Analíticas y Reportes]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#f96,stroke:#333,stroke-width:2px
    style D fill:#9f9,stroke:#333,stroke-width:2px
