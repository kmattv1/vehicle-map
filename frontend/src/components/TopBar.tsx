import React from 'react';
import {createStyles, makeStyles, MuiThemeProvider, Theme} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import {createTheme, FormControl, InputLabel, Select} from "@material-ui/core";

const theme = createTheme({
    palette: {
        primary: {
            light: '#00695f',
            main: '#009688',
            dark: '#33ab9f',
            contrastText: '#fff',
        },
        secondary: {
            light: '#33ab9f',
            main: '#00e5ff',
            dark: '#33eaff',
            contrastText: '#000',
        },
    },
});

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            flexGrow: 1,
        },
        title: {
            flexGrow: 1,
        },
        formControl: {
            margin: theme.spacing(1),
            minWidth: 120,
        },
    }),
);

// @ts-ignore
export default function TopBar(props) {
    const classes = useStyles();

    const [state, setState] = React.useState<{ group: string }>({
        group: 'all',
    });

    const handleChange = (event: React.ChangeEvent<{ name?: string, value: unknown }>) => {
        setState({
            ...state,
            group: event.target.value as string,
        });
        props.onSelectorChange(event.target.value)
    };

    return (
        <div className={classes.root}>
            <MuiThemeProvider theme={theme}>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" className={classes.title}>
                        Vehicles
                    </Typography>
                    <FormControl variant="outlined" className={classes.formControl}>
                        <InputLabel htmlFor="outlined-age-native-simple">Filter</InputLabel>
                        <Select
                            native
                            value={state.group}
                            onChange={handleChange}
                            label="Group"
                            inputProps={{
                                name: 'group',
                                id: 'outlined-group',
                            }}
                        >
                            <option value={"all"}>All</option>
                            <option value={"available"}>Available</option>
                            <option value={"disabled"}>Disabled</option>
                            <option value={"reserved"}>Reserved</option>
                        </Select>
                    </FormControl>
                </Toolbar>
            </AppBar>
            </MuiThemeProvider>
        </div>
    );
}
