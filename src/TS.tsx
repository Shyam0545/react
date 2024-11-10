import React, { useMemo } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from 'material-react-table';
import { data, type Person } from './makeData';
import { useState } from "react";

class App extends React.Component {
    // Constructor
    constructor(props: {}) {
        super(props);
        this.state = {
            items: [],
            DataisLoaded: false,
        };
    }

    // ComponentDidMount is used to
    // execute the code
    componentDidMount() {
        fetch(
            "http://localhost:5555/apache_pinot"
        )
            .then((res) => {
                this.setState({
                    items: res.data,
                    DataisLoaded: true,
                });
            });
    }
}

const Example = () => {
  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        accessorKey: 'agent_id',
        header: 'agent_id',
        size: 200,
      },
      {
        accessorKey: 'call_id',
        header: 'call_id',
        size: 200,
      },
      {
        accessorKey: 'call_start',
        header: 'call_start',
        size: 200,
      },
      {
        accessorKey: 'call_end',
        header: 'call_end',
        size: 200,
      },
      {
        accessorKey: 'call_outcome',
        header: 'call_outcome',
        size: 200,
      },
      {
        accessorKey: 'call_status',
        header: 'call_status',
        size: 200,
      },
      {
        accessorKey: 'company_id',
        header: 'company_id',
        size: 200,
      },
      {
        accessorKey: 'department_id',
        header: 'department_id',
        size: 200,
      },
    {
        accessorKey: 'duration',
        header: 'duration',
        size: 200,
    },
        {
            accessorKey: 'row_id',
            header: 'row_id',
            size: 200,
        },
        {
            accessorKey: 'timestamp',
            header: 'timestamp',
            size: 200,
        },
    ],
    [],
  );

  const table = useMaterialReactTable({
    columns,
    data,
    initialState: { showColumnFilters: true },
  });
  return <MaterialReactTable table={table} />;
};

//Date Picker Imports - these should just be in your Context Provider
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';


const ExampleWithLocalizationProvider = () => (
  //App.tsx or AppProviders file
  <LocalizationProvider dateAdapter={AdapterDayjs}>
    <Example />
  </LocalizationProvider>
);

export default ExampleWithLocalizationProvider;
