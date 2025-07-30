# Phase 1 Analysis: Azure Monitor Documentation Structure

## Overview
This analysis examines the example Azure Monitor documentation files to understand what types of pages need to be generated, the data they contain, potential data sources, and required APIs/technologies.

## Documentation Structure Analysis

Based on examination of the `tools2/examples/reference/` directory, the documentation consists of the following main components:

### Main Index Pages

| Type of page | Data in page | Source of data | API or other technology used |
| ----------- | ------------ | -------------- | ---------------------------- |
| Main Index (`index.md`) | Overview of all reference sections, navigation links to metrics, logs, tables, and queries | Static content structure | Manual content creation |
| Metrics Index (`metrics-index.md`) | List of all platform metrics by resource provider and resource type, links to detailed metric pages | Azure Monitor Metrics API, Resource Provider metadata | Azure Resource Graph, Azure Monitor REST API |
| Logs Index (`logs-index.md`) | List of all resource log categories by resource type, cost information, schema details | Azure Monitor Diagnostic Settings API, Resource Provider metadata | Azure Resource Graph, Azure Monitor REST API |
| Tables Index (`tables-index.md`) | List of Log Analytics tables organized by service, field definitions | Log Analytics Schema API, Table metadata | Azure Monitor Logs REST API, Kusto Schema |
| Tables by Category (`tables-category.md`) | Tables grouped by Azure service categories | Log Analytics table metadata, Service categorization | Azure Resource Graph, Azure Monitor Logs API |
| Queries by Table (`queries-by-table.md`) | Index of sample queries organized by table name | Query examples, table associations | Manual curation with Log Analytics sample queries |

### Detailed Resource Documentation

| Type of page | Data in page | Source of data | API or other technology used |
| ----------- | ------------ | -------------- | ---------------------------- |
| Supported Metrics by Resource (`supported-metrics/microsoft-{provider}-{resourcetype}-metrics.md`) | Resource-specific metrics definitions, units, dimensions, exportability | Azure Monitor Metrics Definitions API | Azure Monitor REST API `/providers/Microsoft.Insights/metricDefinitions` |
| Supported Logs by Resource (`supported-logs/microsoft-{provider}-{resourcetype}-logs.md`) | Resource-specific log categories, diagnostic settings, export costs | Azure Monitor Diagnostic Categories API | Azure Monitor REST API `/providers/Microsoft.Insights/diagnosticSettingsCategories` |

### Table Documentation

| Type of page | Data in page | Source of data | API or other technology used |
| ----------- | ------------ | -------------- | ---------------------------- |
| Table Schema (`tables/{tablename}.md`) | Table field definitions, data types, resource associations, sample queries link | Log Analytics Table Schema | Azure Monitor Logs REST API, Kusto `.show table schema` commands |
| Query Examples (`queries/{tablename}.md`) | Sample KQL queries for specific tables with descriptions | Curated query examples, Log Analytics samples | Manual curation, Log Analytics sample queries API |

### Navigation and Structure

| Type of page | Data in page | Source of data | API or other technology used |
| ----------- | ------------ | -------------- | ---------------------------- |
| Table of Contents (`toc.yml`) | Hierarchical navigation structure for all documentation | Generated from discovered resources and services | Azure Resource Graph for resource provider discovery |

### Reusable Content

| Type of page | Data in page | Source of data | API or other technology used |
| ----------- | ------------ | -------------- | ---------------------------- |
| Include Files (`reusable-content/azure-monitor/reference/`) | Shared content snippets for metrics, logs, and tables | Generated from API responses | Azure Monitor APIs, processed and formatted |



## Critical APIs Required

1. **Azure Resource Graph Query API**: 
   - `POST https://management.azure.com/providers/Microsoft.ResourceGraph/resources`
   - For resource provider and type discovery

2. **Azure Monitor Metrics Definitions API**:
   - `GET https://management.azure.com/subscriptions/{subscription}/providers/Microsoft.Insights/metricDefinitions`
   - For platform metrics discovery

3. **Azure Monitor Diagnostic Settings Categories API**:
   - `GET https://management.azure.com/subscriptions/{subscription}/providers/Microsoft.Insights/diagnosticSettingsCategories`
   - For supported log categories

4. **Azure Monitor Logs REST API**:
   - `POST https://api.loganalytics.io/v1/workspaces/{workspace}/query`
   - For Kusto schema queries and table discovery

## File Generation Patterns

Based on the analysis, files follow consistent naming patterns:

- **Metrics**: `microsoft-{resourceprovider}-{resourcetype}-metrics.md`
- **Logs**: `microsoft-{resourceprovider}-{resourcetype}-logs.md`
- **Tables**: `{tablename}.md` (lowercase)
- **Queries**: `{tablename}.md` (lowercase, matching table names)

## Content Templates Identified

Each file type has a consistent structure with:
- YAML frontmatter with metadata
- Auto-generation disclaimer
- Structured content sections
- Include references to reusable content
- Standardized "Next Steps" sections

## Success Criteria Validation

The generated documentation must exactly match the examples in terms of:
- File naming conventions
- Directory structure
- YAML frontmatter format
- Content organization
- Include file references
- Cross-reference links
- Table of contents hierarchy
