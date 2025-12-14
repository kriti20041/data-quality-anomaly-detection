# Data Quality & Anomaly Detection System

## Problem
In real-world data pipelines, silent data issues such as missing values, invalid ranges, and schema
violations can break analytics and ML systems without immediate visibility.

## Solution
This project demonstrates a data quality monitoring system built on top of Great Expectations-style
validation outputs with a lightweight anomaly detection layer that classifies data issues by severity.

## How It Works
1. Dataset validation rules are applied (simulated using sample validation output)
2. Validation metrics such as failed expectations are collected
3. An anomaly detection script calculates the failure rate
4. Data issues are classified as LOW, MEDIUM, or HIGH severity

## Project Structure
data-quality-anomaly-detection/
├── examples/
│ └── sample_validation.json
├── anomaly_detector.py
└── README.md


## Key Features
- Data quality validation using Great Expectations-style metrics
- Rule-based anomaly detection on validation results
- Severity classification for data reliability monitoring
- Designed to integrate with production ETL and analytics pipelines

## Tech Stack
- Python
- Great Expectations
- JSON-based validation metrics

## Use Cases
- Data pipeline monitoring
- Pre-analytics data validation
- Data reliability checks in production systems
