/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Fragment} from 'react';

import { mapping, light as lightTheme } from '@eva-design/eva';
import { ApplicationProvider, Layout } from 'react-native-ui-kitten';
import { HomeScreen } from './HomeScreen/HomeScreen'

const App = () => (
  <ApplicationProvider
    mapping={mapping}
    theme={lightTheme}>
    <HomeScreen/>
  </ApplicationProvider>
);

export default App;
