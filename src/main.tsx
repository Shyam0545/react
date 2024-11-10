import { StrictMode } from 'react';
import ReactDOM from 'react-dom/client';
import Example from './TS';
import {App} from './api';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <StrictMode>
    <Example />
    <App />
  </StrictMode>,
);
